install.packages("spotifyr")
library(spotifyr)
install.packages("dendextend")
library(dendextend)
library(stats)
install.packages("dplyr")
library(dplyr)

Sys.setenv(SPOTIFY_CLIENT_ID = 'your client id')
Sys.setenv(SPOTIFY_CLIENT_SECRET = 'your client secret')

blink_music <- get_artist_audio_features("blink-182")
duplicated_songs = length(unique(blink_music$track_name)) < nrow(blink_music)
if (duplicated_songs) {
  blink_music <- blink_music %>% distinct(track_name, .keep_all = TRUE)
  blink_music <- blink_music[-c(32:36),]
}

blink_albums <- as.vector(unique(blink_music$album_name))
wanted_features <- as.vector(colnames(blink_music)[c(1,36,30,9:19,22,26,39)])

blink_music_filtered <- blink_music %>%
  filter(album_name %in% blink_albums) %>%
  select(wanted_features) %>%
  mutate(location = 1:n(), key_mode = as.numeric(as.factor(key_mode)))

#album section
blink_album <- blink_music_filtered[blink_music_filtered$album_name=='album name here',]
#blink_album <- blink_album[-14,] #used just for take off your pants and jacket

blink_album_dist <- blink_album %>%
  select(-c("artist_name", "album_name", "track_name")) %>%
  as.matrix() %>%
  scale(center=TRUE, scale=TRUE) %>%
  dist(method = "euclidean")

blink_album_hclust <- hclust(blink_album_dist, method='average')

blink_album_dend <- blink_album_hclust %>% as.dendrogram()

labels(blink_album_dend) <- blink_album$track_name[order.dendrogram(blink_album_dend)]

par(mar = c(2,2,2,12))
par(family = 'Avenir')
blink_album_dend %>%
  set("branches_col", "gray30") %>% 
  set("labels_col", "gray30") %>%
  set("labels_cex", 0.8) %>%
  set("leaves_pch", 15) %>%
  set("leaves_col", 1:nrow(blink_album)) %>%
  set("nodes_cex", 1) %>% 
  plot(horiz = TRUE, main = list(blink_album$album_name[1]), 
                                 cex = 1.5)
