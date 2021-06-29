# Perfect Order Program
This program is designed to give you the "perfect order" which is an order at a restaurant with a user-defined menu and price point as well as a user-defined target price. By running the program the user will receive a list of items from the menu whose prices add up to the exact amount of the target price. If there is no perfect order avaialable a message will indicate such.

## Usage
To run the program, you must have Python 3 installed locally. Download this repo, then in the project folder and from your CLI run 
```bash
python perfect-order.py <path to json file>
```
You will need a json-formatted file to run the program. An example.json is given in the repo. The format is as follows:

```javascript
{
  "target_price": 15.05,
  "menu": {
    "mixed_fruit": 2.15,
    "french_fries": 2.75,
    "side_salad": 3.35,
    "hot_wings": 3.55,
    "mozzarella_sticks": 4.20,
    "sampler_plate": 5.80,
    "something_cheap": 0.15
  }
}
```

If no argument is included in the CLI a message will notify the user. 

Only one perfect order will be given from the program, if there are multiple perfect orders, the first will be given.