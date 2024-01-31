f :: Int -> Int -> Int
f a b
    | a+b==15 = 1
    | otherwise = 2 + f (a-2) (b+1)

main :: IO ()
main = do
    print $ f 20 12
