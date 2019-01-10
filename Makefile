OBJ = src/hello.o

default: $(OBJ)
	mkdir -p lib
	$(CXX) -shared -Wl,-soname,$(SONAME) -o lib/lib$(LIBRARY_NAME).so.$(LIBRARY_VERSION) $^

src/%.o: src/%.cpp
	$(CXX) -c -o $@ $^ -Iinclude -fPIC
