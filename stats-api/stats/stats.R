library(jsonlite)



objarrayToDataframe <- function(json) {
    # Convierte un JSON a un objeto dataframe con formato: array de objetos
    # [{"col1": obs1, "col2": obs1, "..": ..}, {"col1": obs1, "col2": obs1, "..": ..}, {...}]
    # str -> dataframe
    data <- fromJSON(json, simplifyDataFrame=TRUE)
    data <- as.data.frame(data)
    return(data)
}


jsoncolToDataframe <- function(json) {
    # Convierte un JSON a un objeto dataframe con formato: objeto por columna
    # { "index":[1, 2, 3, ...], "column1": [obs1, obs2, obs3, ...], "column2": ...}
    # str -> dataframe
    data <- fromJSON(json, simplifyMatrix=TRUE)
    data <- as.data.frame(data)
    return(data)
}


getMode <- function(value) {
   uniqvalue <- unique(value)
   uniqvalue[which.max(tabulate(match(value, uniqvalue)))]
}


describe <- function(column) {
    # Regresa estadisticas descriptivas basicas
    # list -> list
    description <- list(
        length= length(column),
        min= min(column, na.rm=TRUE),
        max= max(column, na.rm=TRUE),
        mean= mean(column, na.rm=TRUE),
        median= median(column, na.rm=TRUE),
        mode= getMode(column),
        range= range(column, na.rm=TRUE),
        var= var(column, na.rm=TRUE),
        sd= sd(column, na.rm=TRUE),
        quantile= list(
            "0%"= quantile(column, na.rm=TRUE)[1],
            "25%"= quantile(column, na.rm=TRUE)[2],
            "50%"= quantile(column, na.rm=TRUE)[3],
            "75%"= quantile(column, na.rm=TRUE)[4],
            "100%"= quantile(column, na.rm=TRUE)[5]
        )
    )
    return(description)
}

covariance <- function(xvar, yvar) {
    # Regresa la covarianza de dos variables x y y
    # list, list -> numeric
    cov(xvar, yvar, use="complete.obs")
}

covarianceMatrix <- function(variables) {
    # Regresa la covarianza de una matriz
    # matrix -> matrix
    as.data.frame(cov(variables, use="complete.obs"))
}

correlation <- function(xvar, yvar, method) {
    # Regresa la correlacion de dos variables x y y
    # list, list -> numeric
    cor(xvar, yvar, method=method, use="complete.obs")
}

correlationMatrix <- function(variables, method) {
    # Regresa una covarianza de una matriz
    # matrix -> matrix
    as.data.frame(cor(variables, method=method, use="complete.obs"))
}