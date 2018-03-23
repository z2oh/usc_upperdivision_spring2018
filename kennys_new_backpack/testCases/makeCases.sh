#!/bin/sh
PAD="2"

for n in $(seq 0 24)
do
	num=$(printf "%0*d" "$PAD" "$n")
	INPUT_FILE="./input/input$num.txt"
	OUTPUT_FILE="./output/output$num.txt"

	python3 ./testCaseGen.py  > "$INPUT_FILE"
	cat "$INPUT_FILE" | python3 ../solution.py > "$OUTPUT_FILE"
done
