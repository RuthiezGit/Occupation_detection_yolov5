# from bing_images import bing
# from selenium import webdriver
from bing_image_downloader import downloader

# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Replace with the correct path to the ChromeDriver executable

# bing.download_images("lawyer attire",
#                       150,
#                       output_dir=r"C:\Users\USER\Desktop\RAIN\Extra_classes\object detection\lawyers",
#                       pool_size=10,
#                       file_type="png",
#                       force_replace=True,
#                       extra_query_params='&first=1')


downloader.download("thief with an iron rod", 
                    limit=150,  
                    output_dir=r"C:\Users\USER\Desktop\mofi_dataset", 
                    adult_filter_off=True, 
                    force_replace=False, 
                    timeout=60, 
                    verbose=True)