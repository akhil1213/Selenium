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
		driver.findElement(By.linkText("Student Center")).click();
		enroll();
	}
	/*
	 * There is nested html inside of the main html which is inside of one iframe
	 * the child frame has access to enroll anchor tag element, the 2020 spring term input
	 * checkbox, proceed to step 2 of 3 button and finishing enrolling button.
	 * This is why I only change to the child frame once and never change back after logging in and clicking student center.
	 */
	private void enroll() throws InterruptedException {
		/*
		to switch to iframe which has access to enroll anchor tag and clicks on enroll. This frame has acess
		to all of the elements that are needed and the parent hierarchy doesn't have access to any of the elements 
		needed to enroll into a class
		 */
		switchFrame();
		selectTerm();
		/*
		 * we can now select the term because the driver now has the correct iframe
		 * which has html code consisting of all the elements to enroll into a class
		 */
		//driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();
		//driver.findElement(By.xpath("//a[contains(.,'Enroll')]")).click();
//		List<WebElement> elementsxpath = driver.findElements(By.id("win0divPAGECONTAINER"));
//		for ( WebElement w : elementsxpath) {
//			System.out.print(w.getTagName());
//		}
		
//		driver.findElement(By.id("DERIVED_SSS_SCL_SS_ACAD_INFO_LINK")).click();
//		driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();
		//Thread.sleep(2000);
		//System.out.print(driver.findElement(By.id("ptifrmcontent")).getLocation());
		//driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();//click on enroll anchor tag
		//driver.quit();
//		driver.findElement(By.tagName("button")).click(); 
//		System.out.print(driver.findElement(By.id("DERIVED_SCC_SUM_PERSON_NAME")).getText());
	}
	private void switchFrame() {
		WebElement template = driver.findElement(By.id("ptifrmtemplate"));
		WebElement frmcontent =  template.findElement(By.id("ptifrmcontent"));
		WebElement iframe = frmcontent.findElement(By.tagName("iframe"));
		driver.switchTo().frame(iframe);
		driver.findElement(By.name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3")).click();//clicks on enroll
	}
	
	private void selectTerm() {
		driver.findElement(By.id("SSR_DUMMY_RECV1$sels$0$$0")).click();//clicks on 2020 spring term which is still inside iframe
		driver.findElement(By.linkText("Continue")).click();//clicks continue
		finishEnrolling();
	}
	
	//select classes to add, scroll down to find 'finish enrolling' element and then confirm classes
	private void finishEnrolling() {
		try {
			Thread.sleep(5000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//somehow the driver scrolls down by itself to find the link text element 'Proceed to step 2 of 3' and Finish Enrolling anchor tags
		driver.findElement(By.linkText("Proceed To Step 2 Of 3")).click();
		driver.findElement(By.linkText("Finish Enrolling")).click();
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		driver.quit();//close the browser
	}
	//switching frames figured out from stack over flow link: https://stackoverflow.com/questions/9130871/finding-nested-iframe-using-selenium-2
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Selenium s = new Selenium();
			while(true) {
				s.invokeBrowser();
			}
	}
}
