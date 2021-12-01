import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

size = (1200, 1200)

def process_image(img_name):
    # opens image
    img = Image.open(f"multiprocessing/{img_name}")

    # Run image filter with Gaussian Blur
    img = img.filter(ImageFilter.GaussianBlur(15))

    # create an image thumnail of size    
    img.thumbnail(size)
    
    # save image to a processed folder
    img.save(f'multiprocessing/processed/{img_name}')
    print(f'{img_name} was processed...')


if __name__ == "__main__":
    t1 = time.perf_counter()
    
    for img_name in img_names:
        process_image(img_name)

    t2 = time.perf_counter()
    
    print(f'Finished in {t2-t1} seconds\n')
    
    t3 = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
        
    t4 = time.perf_counter()
    
    print(f'Finished in {t4-t3} seconds')