package org.example;

import com.microsoft.playwright.*;
import java.nio.file.Paths;

public class Screenshot {
    public static void main(String[] args) {
        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.webkit()
                    .launch(new BrowserType.LaunchOptions().setHeadless(false).setSlowMo(5000));
            Page page = browser.newPage();
            page.navigate("https://playwright.dev/");
            page.screenshot(new Page.ScreenshotOptions().setPath(Paths.get("example.png")));
        }
    }
}