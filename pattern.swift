let n = Int(readLine()!)!

for i in 0..<n {
    for j in 0..<n {
        let x = i - n / 2
        let y = j - n / 2
        let distance = x * x + y * y

        if distance >= (n / 2 - 1) * (n / 2 - 1) &&
           distance <= (n / 2) * (n / 2) {
            print("1", terminator: " ")
        } else {
            print(" ", terminator: " ")
        }
    }
    print()
}
