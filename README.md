# Develop Number Management HTTP Microservice


## Installation

1. Clone this repository:

```
git clone https://github.com/baukk/testmicro.git
```
2. Navigate to the project directory:
```
cd testmicro
```
Install the required Python packages:
```
pip install -r requirements.txt
```

Make GET requests to /numbers with the url query parameter to retrieve merged numbers from multiple URLs. Example:

http://localhost:3000/numbers?url=http://example.com/api1&url=http://example.com/api2

# outputs
## Solo url output for prime numbers
![solo_prime](https://github.com/baukk/testmicro/assets/76152244/6f9fd5d7-8f49-4fa6-8e99-e16b185bc988)
## Solo url output for odd numbers
![solo_odd](https://github.com/baukk/testmicro/assets/76152244/ba06eb3f-ce6f-47ee-b2b1-7f79c7ea378b)
## Multiple url output for with timeout to 5 second limit (returns two links only)
![multiple_param](https://github.com/baukk/testmicro/assets/76152244/ebb109db-dbf7-4ab9-8900-9f61fc784c45)
## Multiple url output for with no timeout limit (returns all links)
![no timout output](https://github.com/baukk/testmicro/assets/76152244/fa4d3755-c5b7-401f-b269-1ff488c1de08)


