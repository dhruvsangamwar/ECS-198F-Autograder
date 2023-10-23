#include <iostream>
using namespace std;

class Clipboard {
private:
    std::string content;

public:
    void copy(const std::string& text) {
        content = text;
    }

    std::string paste() {
        return content;
    }
};

int main() {
    Clipboard clipboard;

    clipboard.copy("Hello, World!"); // Copy some text to the clipboard
    std::string copiedText = clipboard.paste(); // Paste the text
    std::cout << "Pasted Text: " << copiedText << std::endl;

    return 0;
}