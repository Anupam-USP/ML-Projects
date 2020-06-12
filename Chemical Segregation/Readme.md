# Description
Problem was to segregate the chemical containers into two types: Type 1 and Type 0.

Here I used Logistics Regression classifier to train the dataset, however without the help of sklearn functions. 
They are of better working as rather than iterating, I used the numpy modules. The datasets I used are also attached.
Output is shown as a csv file with column name as label and divides the type of chemicals in either 
**Type 0 or 1** group.


### Cost function visualisation
![error](https://user-images.githubusercontent.com/56446640/84475934-ff8bef00-acaa-11ea-8256-bb9f7d4cca0f.png)


### Dataset visualisation with prediction(Decision Boundary)
![Prediction](https://user-images.githubusercontent.com/56446640/84475840-d8cdb880-acaa-11ea-8d4c-ca7603bf6403.png)


As the error/cost function is continously decreasing we can conclude that logistics regression model is correctly working.
Accuracy of this model is **99%**.