haplotype_accuracy = function(haplotype_exp, haplotype_theor){
  accuracy <- vector()
  for(i in 1:nrow(haplotype_exp)){
    temp <- c(sum((haplotype_exp[i,] == haplotype_theor[i,]) == FALSE)/length(haplotype_exp))
    accuracy <- c(accuracy, 1-temp)
  }
  overall_accuracy <- sum(accuracy)/length(accuracy)
  return(overall_accuracy)
}


  
  