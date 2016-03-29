
is_valid = (a, n, b, m) -> {
  gcd_n_m = gcd(n, m);
  return (Mod(a, gcd_n_m) == Mod(b, gcd_n_m));
}

f = (n, m) -> {
phi_n = eulerphi(n);
phi_m = eulerphi(m);
  if(1-is_valid(phi_n, n, phi_m, m), 0,\
    return (lift(chinese(Mod(phi_n, n), Mod(phi_m, m))));
  );
}

res = 0;
{for(m=1000001,1005000-1,\
  for(n=1000000,m-1,\
    res = res + f(n,m);
))}
print(res)
