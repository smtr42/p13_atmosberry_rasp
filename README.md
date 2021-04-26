<h1 align="center">
Project 13 - Atmosberry Raspberry Client
</h1>

<p align="center">
  <a href="">
    <img src="https://upload.wikimedia.org/wikipedia/fr/0/0d/Logo_OpenClassrooms.png" alt="Logo" width="100" height="100">
  </a>
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8-green.svg">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg">
  </a>
  <a href="https://www.linkedin.com/in/teiva-s/">
    <img src="https://img.shields.io/badge/linkedin-Simonnet-blue.svg">
  </a>
</p>


  <h3 align="center">PART 2 :Final project from the OpenClassrooms Python course.</h3>

 <p align="center">
    Client used to send data to the website
    <br />
  </p>

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <a href="https://fr.openfoodfacts.org/">
    <img src="https://upload.wikimedia.org/wikipedia/fr/3/3b/Raspberry_Pi_logo.svg" width=55>
  </a>
</p>

As an ex-meteorologist I like to forecast the weather and tech people about it. In this project i attempt to sensitize people about the weather and climate change. 

People would have a cheap raspberry and a few sensors they can visualize online. A map will display all raspberry online and sharing data. People will take part in a utopically widespread open-source project.

[Original server repo for P13](https://github.com/smtr42/p13_atmosberry2)

<!-- GETTING STARTED -->
## Getting Started

#### Live version
The website is hosted on heroku  [on this link](http://www.simteiva.fr/)


## Usage

* First you connect to [the site](http://www.simteiva.fr/) and create an account.
* Once connected, you go to your [dashboard](http://www.simteiva.fr/dashboard) and click on the refresh token button to create a token.

At this point you will have access to the API and you will need to use the token to authenticate.

* Use the form to register a raspberry on the website and give it its coordinates in decimal degrees.


### Send data

To send data you will have multiple ways. The endpoint to use is: http://www.simteiva.fr/api/v1/

The format of the body you send should look like this:
```python
{
    "sensor_type": "type",
    "device": "name of the device",
    "measure": the measure,
    "timestamp": thedate,
    "name": "name of the sensor",
}
```

* `sensor_type` can only have 3 types possibility: "T", "Hu" and "P"
* The `device` must be registered before sending data to it, and you must setup the exact same name>
* `measure` is the measure of the sensor as a float.
* `timestamp` is the date in format `2021-04-19T16:36:50Z`
* `name`is the name of the sensor.


### Authentication

You must set your header as such:
`"Authorization": Token {yourtoken}`

### How
*  Clone the repo
```bash
$ git clone https://github.com/smtr42/p13_atmosberry_rasp
```
*  Install required dependencies
```bash
$ pip install -r requirements.txt
```

For the sake of evaluation I put a dummy openweathermap process getting data from Lyon and sending it to the website.

You must set up your environment variables in a .env file.
One is necessary to acces the website : token
You use the token generated on the website to access it.

A second variable is optional : weather_token
You must register and ask an API key on openweathermap to have one.

*  Launch Script
```bash
$ python -m main
```

Look at your profile on the website and in the dashboard you will see th newly data on the graph.

### Links
Used in the project:
* [Black](https://pypi.org/project/black/)

## Author
[Project Link](https://github.com/smtr42/p13_atmosberry2)

* **Simonnet T** - *Initial work* - [smtr42](https://github.com/smtr42)
   
  <a href="https://www.linkedin.com/in/teiva-s/">
   <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg" alt="linkedin" width="200" height="54">
 </a>
<br>