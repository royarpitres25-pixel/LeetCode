#!/usr/bin/env bash
# Build and run a LeetCode problem's basecode driver, no matter whether the
# file you have open/pass in is the bare solutions/ snippet (no main()) or
# the basecode/ driver itself.
#
# Usage: scripts/run.sh <path-to-cpp-file>
#   e.g. scripts/run.sh solutions/prefixsum/RangeSumQueryImmutable303.cpp
#        scripts/run.sh basecode/prefixsum/RangeSumQueryImmutable303.cpp

set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <path-to-cpp-file>" >&2
    exit 1
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
REL="${INPUT#"$REPO_ROOT"/}"

if [[ "$REL" == solutions/* ]]; then
    # Driver filename may not exactly match the solution's (e.g. a "Runner"/
    # "Test" suffix), so find it by glob within the matching basecode/{pattern}
    # folder instead of assuming an identical basename.
    SUB_PATH="${REL#solutions/}"
    PATTERN_DIR="$(dirname "$SUB_PATH")"
    NAME="$(basename "${SUB_PATH%.cpp}")"
    SEARCH_DIR="$REPO_ROOT/basecode/$PATTERN_DIR"

    matches=()
    if [[ -d "$SEARCH_DIR" ]]; then
        while IFS= read -r -d '' f; do
            matches+=("$f")
        done < <(find "$SEARCH_DIR" -maxdepth 1 -type f -name "${NAME}*.cpp" -print0)
    fi

    if [[ ${#matches[@]} -eq 0 ]]; then
        echo "No basecode driver found under basecode/$PATTERN_DIR matching ${NAME}*.cpp" >&2
        exit 1
    elif [[ ${#matches[@]} -gt 1 ]]; then
        echo "Multiple basecode drivers match ${NAME}*.cpp, pick one explicitly:" >&2
        printf '  %s\n' "${matches[@]}" >&2
        exit 1
    fi
    DRIVER_PATH="${matches[0]}"
elif [[ "$REL" == basecode/* ]]; then
    DRIVER_PATH="$INPUT"
else
    echo "Not under solutions/ or basecode/: $REL" >&2
    exit 1
fi

DRIVER_REL="${DRIVER_PATH#"$REPO_ROOT"/}"
if [[ ! -f "$DRIVER_PATH" ]]; then
    echo "No basecode driver found at $DRIVER_REL (expected the counterpart of $REL)" >&2
    exit 1
fi

BIN_DIR="$REPO_ROOT/.build"
mkdir -p "$BIN_DIR"
BIN_PATH="$BIN_DIR/$(basename "${DRIVER_REL%.cpp}")"

echo "Building $DRIVER_REL ..."
clang++ -std=c++17 -Wall -g "$DRIVER_PATH" -o "$BIN_PATH"

echo "Running $(basename "$BIN_PATH") ..."
echo "-----------------------------------"
"$BIN_PATH"
