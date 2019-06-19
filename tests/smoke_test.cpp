#include <gtest/gtest.h>
#include <spdlog/spdlog.h>
#include <map>
#include <random>

GTEST_TEST(SmokeTest, SmokeTest) {
  SPDLOG_INFO("running tests");
  ASSERT_TRUE(true);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}