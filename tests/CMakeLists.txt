add_executable(smoke_test smoke_test.cpp)
target_link_libraries(smoke_test gtest_main spdlog::spdlog)
gtest_add_tests(TARGET smoke_test)
