## Indian Economy Presentation 

This is the replication package for the lecture on `SHRUG: Using data to understand the Indian Economy`. 
Go through this repo to recreate the results and graphs in the presentation/jupyter notebook. 

### Structure 

- All the data here comes from the publicly available SHRUG (Socioeconomic High-resolution Rural-Urban Geographic Platform for India). Subset of the Data for this lecture can be downloaded from [here](https://drive.google.com/file/d/1TqAJyfFxircvKkcZIYb2U0INAqAIyvIW/view?usp=sharing)
    - Some datasets have been processed beforehand in the intrests of time.
        1. `~/data/indian_economy_lecture/ec_dist.dta`
        2. `~/data/indian_economy_lecture/ec_subdist.dta`
        3. `~/data/indian_economy_lecture/ec_india_summary.dta`
    - Dataset cleaning code: `~/indian_economy/prep_data.do`
       - Cleaning code is in stata just in case anyone prefers that coding language and is disappointed that we did everything else in Python. 
       - The first graph on employment across sectors from ec can also be generated within the `prep_data.do` code itself. 
- The main analysis exists in `~/indian_economy/indian_economy_pres.ipynb`
       
###  Getting python to run locally

The ipython notebook/html can be run locally on your desktop in either an IDE like Anaconda or through the command line with miniconda. 
- I'd recommend Anaconda if you're very new to Python. Documentation [here](https://docs.anaconda.com/_downloads/3613d324acc0a4b3c203fd79c71a2b45/Anaconda-Starter-Guide.pdf)
    - And you're set to run Jupyter notebooks (in python) from Anaconda locally. 
- At the very least you'd need to install the packages pandas, geopandas, matplotlib and numpy. We use one custom function called make_heatmap() to create geographic maps of ec/pc data in `~/indian_economy/tools.py`. Whichever directory you save the tools.py function in, make sure to tell python to search for this function in there using the lines:
``` python
sys.path.insert(0, '/path/to/folder/with/tools.py')
from tools import make_heatmap
```

### Running the code
Once you have python/jupyter notebooks setup on your desktop you should be able to run this notebook or code locally. 


    

        

