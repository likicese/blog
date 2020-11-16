// stteam的小测试

public static void main(String[] args){
   List<String> s = new ArrayList<>();
   s.add("a");
   s.add("b");
   s.add("c");
   s.add("d");
   s.add("e");
   System.out.println(s);
   s = s.stream().filter(e -> !"d".equals(e)).collect(Collectors.toList());
   System.out.println(s);
}