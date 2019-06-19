add_executable(smoke_test smoke_test.cpp)
target_link_libraries(smoke_test Catch2::Catch2 spdlog::spdlog)
