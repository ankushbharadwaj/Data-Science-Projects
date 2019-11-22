install.packages("spotifyr")

library(spotifyr)

Sys.setenv(SPOTIFY_CLIENT_ID = '1a272511b1a34923bf22994d93e1c502')
Sys.setenv(SPOTIFY_CLIENT_SECRET = 'ad2c0abffd264237878769d1d2f830a1')

blink_music <- get_artist_audio_features("blink-182")
duplicated_songs = length(unique(blink_music$track_name)) < nrow(blink_music)
if (duplicated_songs) {
  blink_music <- blink_music %>% distinct(track_name, .keep_all = TRUE)
  blink_music <- blink_music[-c(32:36),]
}

blink_albums <- as.vector(unique(blink_music$album_name))
wanted_features <- as.vector(colnames(blink_music)[c(1,36,30,9:19,22,26,39)])

install.packages("dplyr")
library(dplyr)

blink_music_filtered <- blink_music %>%
  filter(album_name %in% blink_albums) %>%
  select(wanted_features) %>%
  mutate(location = 1:n(), key_mode = as.numeric(as.factor(key_mode)))

install.packages("dendextend")

library(dendextend)
library(stats)

blink_music_dist <- blink_music_filtered %>%
  select(-c("artist_name", "album_name", "track_name")) %>%
  as.matrix() %>%
  scale(center=TRUE, scale=TRUE) %>%
  dist(method = "euclidean")

blink_music_hclust <- hclust(blink_music_dist, method='average')

blink_music_dend <- blink_music_hclust %>% as.dendrogram()

colors_to_albums <- blink_music$album_name %>%
  recode('NINE' = 'chartreuse', 'California' = 'yellow',
         'blink-182' = 'violetred1', 'Take Off Your Pants And Jacket' = 'gray0',
         'Enema Of The State' = 'darkslateblue', 'Buddha' = 'darkorange',
         'Dude Ranch' = 'firebrick1', 'Cheshire Cat' = 'goldenrod3')
colors_to_albums <- colors_to_albums[order.dendrogram(blink_music_dend)]

labels(blink_music_dend) <- blink_music$track_name[order.dendrogram(blink_music_dend)]

par(mar = c(2,2,2,12))
par(family = 'Avenir')
blink_music_dend %>%
  set("branches_col", "gray30") %>% 
  set("labels_col", "gray30") %>%
  set("labels_cex", 0.2) %>%
  set("leaves_pch", 15) %>%
  set("leaves_col", colors_to_albums) %>%
  set("nodes_cex", 0.5) %>% 
  plot(horiz = TRUE, main = list("blink-182 Song Similarity", cex = 1.5))
legend("topleft", cex = 0.5, title = 'Album',  
       legend = c(paste(unique(blink_music$album_name), 
                        unique(blink_music$album_release_year), 
                        sep = " - ")), 
       fill = c('chartreuse', 'yellow', 'violetred1', 
                'gray0', 'darkslateblue', 'darkorange', 'firebrick1', 'goldenrod3'))

install.packages("reshape2")
library(reshape2)

blink_album_avg <- blink_music_dist %>%
  as.matrix() %>%
  as.data.frame() %>%
  mutate(album_name = blink_music_filtered$album_name) %>%
  reshape2::melt(id = 'album_name') %>%
  mutate(variable = as.numeric(as.character(variable))) %>%
  left_join(blink_music_filtered[, c('location','album_name')], by = c('variable' = 'location')) %>%
  group_by(album_name.x, album_name.y) %>%
  summarise(distance = median(value)) %>%
  reshape2::dcast(album_name.x ~ album_name.y,
                  value.var = 'distance')

dend_blink_album <- blink_album_avg %>%  
  select(-album_name.x) %>% 
  as.dist() %>% 
  hclust(method = 'average') %>%
  as.dendrogram()

par(mar = c(5,2,5,14))  
dend_blink_album %>%  
  set("nodes_cex", 0.85) %>%
  set("leaves_pch", 19) %>%
  set("leaves_col", c('violetred1', 'darkorange', 'yellow', 
                      'goldenrod3', 'firebrick1', 'darkslateblue',
                      'chartreuse', 'gray0')) %>%
  plot(horiz = TRUE, main = list("blink-182 Album Similarity", cex = 1.5))

