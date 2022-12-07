from collections import defaultdict
import os
from pathlib import Path
import re
from typing import Dict, List, Optional
from operator import itemgetter


MAX_SIZE: int = 100000
TOTAL_AVAILABLE: int = 70000000
MINIMUM_NEEDED: int = 30000000


def parse_cd(line: str, path: List[str]) -> List[str]:
    if "$ cd .." in line:
        path.pop()
        return path
    elif "$ cd /" in line:
        return ["/"]
    else:
        path.append(line[5:].strip())
        return path


def get_file_size(line: str) -> Optional[int]:
    size = re.search("^(\d+)", line)
    if not size:
        return None
    else:
        return int(size.group(1))


def main(file_name):
    data_file = Path(os.path.dirname(__file__)) / file_name
    dir_sizes: Dict[str, int] = defaultdict(int)
    path: List[str] = []
    with open(data_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("$ cd"):
                path = parse_cd(line, path)
            elif line.startswith("$ ls"):
                continue
            else:
                size = get_file_size(line)
                if size:
                    for i, _ in enumerate(path):
                        dir_sizes["/".join(path[: i + 1])] += size

    print(
        f"PART 1  Sum of directories smaller than {MAX_SIZE}: {sum([v for v in dir_sizes.values() if v <= MAX_SIZE])}"
    )
    unused_space = TOTAL_AVAILABLE - dir_sizes["/"]
    to_clear_for_update = MINIMUM_NEEDED - unused_space
    candidates = {k: v for k, v in dir_sizes.items() if v >= to_clear_for_update}
    print(
        f"PART 2  Directory to delete for update: {sorted(candidates.items(), key=itemgetter(1))[0]}"
    )


if __name__ == "__main__":
    main("test.txt")
