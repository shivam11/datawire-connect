class Overload {
    Overload add(Overload o) {
        return o;
    }

    void test() {
        Overload o1 = Overload();
        Overload o2 = Overload();
        Overload o3 = o1 + o2;
    }
}
