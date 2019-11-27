billboard_data <- read.csv("/Users/ankushbharadwaj/Desktop/billboard_lyrics_1964-2015.csv",
                           header = TRUE)

if (sum(is.na(billboard_data$Song)) != 0)
  print("missing song")

if (sum(is.na(billboard_data$Artist)) != 0)
  print("missing artist")

library(spotifyr)
Sys.setenv(SPOTIFY_CLIENT_ID = 'your spotify client id')
Sys.setenv(SPOTIFY_CLIENT_SECRET = 'your spotify client secret')

library(dplyr)

test <- get_artist_audio_features("sam the sham and the pharaohs")
test <- test[tolower(test$track_name)=="wooly bully",]
wanted_features <- as.vector(colnames(test)[c(1,36,30,9:19,22,26,39)])
test <- test %>% 
  select(wanted_features) %>%
  distinct(track_name, .keep_all = TRUE)

new_billboard_df <- test

for (i in c(2:nrow(billboard_data))) {
  tryCatch({
  artist <- as.character(billboard_data$Artist[i])
  song <- as.character(billboard_data$Song[i])
  temp <- get_artist_audio_features(artist = artist)
  temp <- temp[gsub("[[:punct:]]", "", tolower(temp$track_name))== song,]
  temp <- temp %>% 
    select(wanted_features) %>%
    distinct(track_name, .keep_all = TRUE)
  new_billboard_df <- rbind(new_billboard_df, temp)}, error=function(e){} )
}

save_new_df <- new_billboard_df

new_billboard_df$track_name_1 <- new_billboard_df$track_name %>% tolower()
new_billboard_df$track_name_1 <- as.vector(gsub("[[:punct:]]", "", new_billboard_df$track_name_1))
new_billboard_df <- new_billboard_df %>% distinct(track_name_1, .keep_all = TRUE)

new_billboard_df$year <- rep.int(0, nrow(new_billboard_df))

save_new_df_1 <- new_billboard_df

for (i in c(1:nrow(new_billboard_df))) {
  tryCatch({
  if (sum(new_billboard_df$track_name_1[i] == billboard_data$Song) == 1) {
    new_billboard_df$year[i] <- 
      billboard_data[billboard_data$Song == new_billboard_df$track_name_1[i],]$Year
  }
  }, error=function(e){})
}

sum(new_billboard_df$year == 0)
#336
if (sum(is.na(new_billboard_df$track_name_1)) != 0)
  print("missing song")
if (sum(is.na(new_billboard_df$artist_name)) != 0)
  print("missing artist")

new_billboard_df <- new_billboard_df[new_billboard_df$year != 0,]
new_billboard_df <- new_billboard_df %>% 
  mutate(location = 1:n(), key_mode = as.numeric(as.factor(key_mode)))
final_billboard_df <- new_billboard_df

library(stats)
library(reshape2)

billboard_df_dist <- final_billboard_df %>%
  select(-c("artist_name", "album_name", "track_name", "track_name_1", "year")) %>%
  as.matrix() %>%
  scale(center=TRUE, scale=TRUE) %>%
  dist(method = "euclidean")

billboard_dist_avg <- billboard_df_dist %>%
  as.matrix() %>%
  as.data.frame() %>%
  mutate(year = final_billboard_df$year) %>%
  reshape2::melt(id = 'year') %>%
  mutate(variable = as.numeric(as.character(variable))) %>%
  left_join(final_billboard_df[, c('location','year')], by = c('variable' = 'location')) %>%
  group_by(year.x, year.y) %>%
  summarise(distance = median(value)) %>%
  reshape2::dcast(year.x ~ year.y,
                  value.var = 'distance')

library(dendextend)

dend_billboard <- billboard_dist_avg %>%  
  select(-year.x) %>% 
  as.dist() %>% 
  hclust(method = 'average') %>%
  as.dendrogram()

par(mar = c(5,1,5,1))  
dend_billboard %>%  
  set("labels_cex", 0.4) %>%
  set("nodes_cex", 0.5) %>%
  set("leaves_pch", 19) %>%
  set("leaves_col", c(1:nrow(billboard_dist_avg))) %>%
  plot(horiz = TRUE, 
       main = list("Differences in Billboard Charts from 1965-2015", cex = 1.5))

