lCP :: [String] -> String
--if list empty
lCP [] = []
--if first word is empty    
lCP ([]:xs) = [] 
--take first char in word as CP to check and mark the first word as accepted in this CP
lCP ((x:xs):xss) = prefix (xss) [x:xs] [x]

prefix :: [String] -> [String]-> String -> String
--if accepted words take another char from first word in accepted list add it to CP to check and accept word
prefix [] (x:lst) cp | length x > length cp = prefix lst [x] (take ((length cp)+1) x)
                          --if first word is not longer than the CP, this == LCP
                          | otherwise = cp                                                      

--check current word and if accepted, mark it and check the next one
prefix (x:xs) lst cp | length x >= length cp && (take (length cp) x) == cp = prefix xs (x:lst) cp
                          --if one fails then the last CP is LCP so ignore last char 
                          | otherwise = init cp

