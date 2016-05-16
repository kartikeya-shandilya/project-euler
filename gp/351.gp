
farey_len = (x) -> {
  res = (3 + sum(d=1, x, moebius(d)*(x\d)^2))/2;
  return(res);
}

hexa = (x) -> {
  res = 3*x*(x+1) - 6*(farey_len(x)-1);
  return(res);
}

hexa(1000)
