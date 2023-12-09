local vals = {
    ["0"]=0,
    ["1"]=1,
    ["2"]=2,
    ["3"]=3,
    ["4"]=4,
    ["5"]=5,
    ["6"]=6,
    ["7"]=7,
    ["8"]=8,
    ["9"]=9,
}

local sum = 0
for line in io.lines() do
    first = nil
    last = nil
    for i = 1, #line do
        for k, v in pairs(vals) do
            if string.sub(line, i, i + #k - 1) == k then
                if first == nil then
                    first = k
                end
                last = k
            end
        end
    end
    sum = sum + (first * 10) + last
end
print(sum)
