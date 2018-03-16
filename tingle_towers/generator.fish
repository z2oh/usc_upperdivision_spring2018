for i in (seq 10)
    echo 100 100 100 | python generator.py > ./test_cases/input/input(math $i'+20').txt
end
