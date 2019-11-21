FROM haoxiangpeng/latest-cpp

COPY . /usr/src/template
WORKDIR /usr/src/template
RUN mkdir build_tmp && cd build_tmp && cmake -DCMAKE_BUILD_TYPE=Release .. && make
ENTRYPOINT make -C build_tmp test ARGS="-E logging -T Test"
