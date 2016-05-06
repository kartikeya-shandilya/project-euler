
z = 1000000007;
n = 1000000;
ans = sum(k=1, n, Mod(k^2-1, z) * ((-1)^(n%2)*Mod((k^2-1), z)^n - 1) * Mod(1/k^2, z));
print(ans)
