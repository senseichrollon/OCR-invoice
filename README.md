# OCR-invoice

## Inspiration
Extracting, processing, and analyzing data is becoming an increasingly important part of many industries. One such form of data-processing is called document analysis in which documents and images can be easily transcribed using machine learning. We decided to look at a specific type of document called an ‘Invoice,” which is a commercial document that contains information about sales transactions.

## What it does
OCR Invoice is a python application that requests Invoice data, in the form of image or pdf files, and extracts all of the relevant information. After processing the data, we output a structured CSV file that the user can save to their machine.

## How we built it
In order to handle the challenge of converting the image data into processable text, we implemented Google Cloud’s Vision API into our project. After this conversion, we used python to re-structure the data into different categories and output the data into a CSV file

## Challenges we ran into
The process of integrating the Google Cloud VIsion API into our code was a long and tedious process that took lots of troubleshooting and stack overflow searches to end successfully. We also had a lot of trouble trying to process the data that we extracted from the invoice files since that data was extracted in a very unorganized format.

## Accomplishments that we're proud of
While we still need some more time perfecting our data-processing algorithms to work over all types of invoice files, we were proud that we managed to organize the data in the invoice file with high accuracy for many of the sample files we were given.

## What we learned
We learned a great deal about pip and python installations since it took us a big bulk of time to even get set up with google cloud. We also learned a lot about how to use Google Cloud, and even Python in general since our team was comprised mostly of C++ developers.

## What's next for OCR Invoice
In the coming months, we will likely be working on honing the data-processing algorithms that organize the extracted data so that it can work with near-perfect accuracy. In addition to this, we may consider upgrading our UI from a simple python GUI to a fully-fledged web application.

		

