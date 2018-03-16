set cases (math (random)'%10+5')
echo $cases
for J in (seq $cases)
    echo 256
    ./rgg -c .7 -n 256
end
