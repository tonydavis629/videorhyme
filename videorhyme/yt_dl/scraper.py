from selenium import webdriver
from selenium.webdriver.common.by import By


def get_video_results(query: str, num_pages: int):
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/results?search_query=' + query)
    # driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
 
    youtube_data = []

    i = 0
    while i < num_pages:
        # iterate over all elements and extract link
        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        i += 1
   
        for result in driver.find_elements(By.CLASS_NAME, 'text-wrapper.style-scope.ytd-video-renderer'):  
            link = result.find_element(By.CSS_SELECTOR, '.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
            title = result.find_element(By.CSS_SELECTOR, '.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('title')
            channel = result.find_element(By.CLASS_NAME, 'long-byline.style-scope.ytd-video-renderer').text
            views = result.find_element(By.CLASS_NAME, 'style-scope.ytd-video-meta-block').text.split(' ')[0]
            youtube_data.append({'title': title, 'link': link, 'channel': channel, 'views': views})

    driver.quit()
    return youtube_data

print(get_video_results(query = 'al gore', num_pages = 1))