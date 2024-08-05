#include <iostream>
#include <string>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>

std::string extensionId = "com.gabeochoa.openinprofile";
std::string appName = "Open In Profile Native";

#include <iostream>
#include <string>

int main() {
  while (1) {
    unsigned int length = 0;

    // Neat way!
    for (int i = 0; i < 4; i++) {
      unsigned int read_char = getchar();
      length = length | (read_char << i * 8);
    }

    // read the json-message
    std::string msg = "";
    for (int i = 0; i < length; i++) {
      msg += getchar();
    }

    std::string message = "{\"text\":\"This is a response message\"}";
    // Collect the length of the message
    unsigned int len = message.length();

    // Now we can output our message
    if (msg == "{\"text\":\"#STOP#\"}") {
      message = "{\"text\":\"EXITING...\"}";
      len = message.length();

      std::cout << char(len >> 0) << char(len >> 8) << char(len >> 16)
                << char(len >> 24);

      std::cout << message;
      break;
    }

    // return stdin message
    len = length;
    std::cout << char(len >> 0) << char(len >> 8) << char(len >> 16)
              << char(len >> 24);

    std::cout << msg << std::flush;

    // return response message
    // std::cout    << char(len>>0)
    //          << char(len>>8)
    //          << char(len>>16)
    //          << char(len>>24);
    //
    // std::cout << message << std::flush;

    // Open the URL in an external application
    // std::string command = "open \"" + url + "\"";
    // system(command.c_str());
    // std::cout << "running command : " << command << std::endl;
  }

  return 0;
}
