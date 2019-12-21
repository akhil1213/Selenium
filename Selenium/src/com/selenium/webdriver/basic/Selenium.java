package com.selenium.webdriver.basic;//increases readability of our code, package tells us the purpose of this code

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Selenium {
	WebDriver driver;//Selenium WebDriver drives a browser natively, as a real user would, either locally or on remote machines.
	public void invokeBrowser() {
		try {
			System.setProperty("webdriver.chrome.driver","/Users/akhilkhanna/Downloads/chromedriver");
			driver = new ChromeDriver();//the browser i'm using is chrome so I need a chrome driver.
			driver.manage().deleteAllCookies();
			driver.manage().window().maximize();//driver opens the browser in a minimized size
			driver.get("http://www.amazon.com");
			search();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void search() {
		//driver.findElement(By.linkText("Players")).click();
		driver.findElement(By.id("twotabsearchtextbox")).sendKeys("lebron");
		driver.findElement(By.xpath("//input[@type='submit' and @value='Go']")).click();
		
//		List<WebElement> listOfElements = driver.findElements(By.className("nav-input"));
//		for(WebElement we : listOfElements) {
//			System.out.print(we.getTagName());
//		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Selenium s = new Selenium();
			s.invokeBrowser();
	}
}
