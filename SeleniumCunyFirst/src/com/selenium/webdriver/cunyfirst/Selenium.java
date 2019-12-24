package com.selenium.webdriver.cunyfirst;

import java.util.List;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;



public class Selenium {
	WebDriver driver;//Selenium WebDriver drives a browser natively, as a real user would, either locally or on remote machines.
	public void invokeBrowser() {
		try {
			System.setProperty("webdriver.chrome.driver","/Users/akhilkhanna/Downloads/chromedriver");
			driver = new ChromeDriver();//the browser i'm using is chrome so I need a chrome driver.
			//driver.manage().deleteAllCookies();
			driver.manage().window().maximize();//driver opens the browser in a minimized size
			driver.get("https://home.cunyfirst.cuny.edu/psp/cnyepprd/EMPLOYEE/EMPL/h/?tab=DEFAULT");
			driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
			login();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	private void login() throws InterruptedException {
		driver.findElement(By.id("CUNYfirstUsernameH")).sendKeys("akhil.khanna52@login.cuny.edu");
		driver.findElement(By.id("CUNYfirstPassword")).sendKeys("Akhil23525052");
		Thread.sleep(2000);
		driver.findElement(By.tagName("button")).click();
		//driver.quit();
		enroll();
	}
	private void enroll() throws InterruptedException {
		driver.findElement(By.linkText("Student Center")).click();
		//driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();
		//driver.findElement(By.xpath("//a[contains(.,'Enroll')]")).click();
//		List<WebElement> elementsxpath = driver.findElements(By.id("win0divPAGECONTAINER"));
//		for ( WebElement w : elementsxpath) {
//			System.out.print(w.getTagName());
//		}
		
//		driver.findElement(By.id("DERIVED_SSS_SCL_SS_ACAD_INFO_LINK")).click();
//		driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();
		Thread.sleep(2000);
		//System.out.print(driver.findElement(By.id("ptifrmcontent")).getLocation());
		switchFrame();//to switch to iframe which has access to enroll anchor tag and clicks on enroll
		//driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();//click on enroll anchor tag
		//driver.quit();
//		driver.findElement(By.tagName("button")).click(); 
//		System.out.print(driver.findElement(By.id("DERIVED_SCC_SUM_PERSON_NAME")).getText());
		selectTerm();
	}
	private void switchFrame() {
		WebElement template = driver.findElement(By.id("ptifrmtemplate"));
		WebElement frmcontent =  template.findElement(By.id("ptifrmcontent"));
		WebElement iframe = frmcontent.findElement(By.tagName("iframe"));
		driver.switchTo().frame(iframe);
		driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();
	}
	
	private void selectTerm() {
		driver.findElement(By.id("SSR_DUMMY_RECV1$sels$0$$0")).click();
		driver.findElement(By.linkText("Continue")).click();
		finishEnrolling();
	}
	private void finishEnrolling() {
		driver.findElement(By.linkText("Proceed To Step 2 Of 3")).click();
		//the driver doesn't see the finish enrolling button element since it's not visible so I have to scroll down.
		JavascriptExecutor jse = (JavascriptExecutor)driver;
		jse.executeScript("window.scrollBy(0,500)");
		driver.findElement(By.linkText("Finishing Enrolling")).click();
	}
	//switching frames figured out from stack over flow link: https://stackoverflow.com/questions/9130871/finding-nested-iframe-using-selenium-2
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Selenium s = new Selenium();
			s.invokeBrowser();
	}
}
