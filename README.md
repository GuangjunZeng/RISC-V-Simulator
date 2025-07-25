## Project Compilation

```bash


# Make a build folder
mkdir build
cd build

# Build the project
cmake ..
make
```

## Project Structure

- `src`: Source code
- `include`: ELFIO headers
- `test-*`: Test case folders
- `part2.s`: The part2.s file. You can put part2_p2.s / part2_p3.s at the root path of the project.

## Useful Scripts

You can use `bash <script_name>` to run the scripts.

- `build-test.sh`: Builds ELF files for the following test cases. You can find the ELF files and objdumped files under `/riscv-elf`:
  - `build-test-basic.sh`
  - `build-test-inclass.sh`
  - `build-test-fused.sh`
  - `build-part2.sh`
- `run-simulator.sh`: Runs all ELF files under `/riscv-elf` and outputs results to `/results`;
- `run-simulator-without-data-forwarding.sh` : Run all ELF files without data forwarding.

## Quick Run

```bash
bash build-test.sh
bash run-simulator.sh
bash run-simulator-without-data-forwarding.sh
```

## Usage

```
./Simulator riscv-elf-file-name [-v] [-s] [-d] [-x] [-b strategy]
```
Parameters:

1. `-v` for verbose output, can redirect output to file for further analysis.
2. `-s` for single step execution, often used in combination with `-v`.
3. `-d` for creating memory and register history dump in `dump.txt`.
4. `-b` for branch perdiction strategy (default `BTFNT`), accepted parameters are `AT`, `NT`, `BTFNT`. and `BPB`. **You can ignore this one in this assignment**.
5. `-x` for disabling data forwarding. **You need to implement this one**.

**Hint: You can use -v -s for debugging.**

## Expected Results

| Test case     | Data forwarding? | Handle WriteBack before Decode? \* | Cycles |
|---------------|------------------|---------------------------------|--------|
| ackermann     | ✔️                | /                               | 480358 |
| ackermann     | ❌                | ✔️                               | 623850 |
| ackermann     | ❌                | ❌                               | 719706 |
| fmadd / fmsub | ✔️                | /                               | 813    |
| fmadd / fmsub | ❌                | ✔️                               | 1005   |
| fmadd / fmsub | ❌                | ❌                               | 1113   |
| fnm           | ✔️                | /                               | 811    |
| fnm           | ❌                | ✔️                               | 1002   |
| fnm           | ❌                | ❌                               | 1109   |

\* Whether you handle WriteBack before Decode or not, we will give you full marks. If you are not aware of this case, please review the lecture: Page 12, Chapter 4: Pipeline Hazards.
