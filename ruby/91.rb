
count = 0
len = 50
0.upto len do |x1|
  0.upto len do |y1|
    0.upto len do |x2|
      0.upto y1 do |y2|
        break if x1 == x2 && y1 == y2 ||
          x2 == 0 && y2 == 0 || x1 == 0 && y1 == 0
        count += 1 if x1*x2+y1*y2 == 0 ||
          x1*(x2-x1) + y1*(y2-y1) == 0 || x2*(x2-x1) + y2*(y2-y1) == 0
      end
    end
  end
end
puts count
