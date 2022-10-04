const fs = require('fs')
function sieve(n) {
    let A = Array(n).fill(true);
    let roof = Math.ceil(Math.sqrt(n))
    for (let i = 2; i<roof; i++) {
        if (A[i]) {
            for (let j = i*i; j < n; j+=i) {
                A[j] = false;
            }
        }
    }
    let primes = A.map((b,i)=>b && i)
    return primes.filter(x=>x).slice(1)
}


fs.writeFile("primes.json", JSON.stringify(sieve(1e7)), x=>x)