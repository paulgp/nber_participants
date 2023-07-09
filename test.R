read_csv("participants.csv", col_names = FALSE)

ggplot(data = read_csv("participants.csv", col_names = FALSE) %>%
    mutate(X1 = stringr::str_replace_all(X1, "SI 2023 ", ""))) +
    geom_col(aes(y = X2, x = reorder(X1, -X2))) +
    coord_flip() +
    labs(x = "Session", y = "Number of Registered Participants")

ggplot(data = read_csv("participants.csv", col_names = FALSE) %>%
    filter(X2 < 600) %>%
    mutate(X1 = stringr::str_replace_all(X1, "SI 2023 ", ""))) +
    geom_col(aes(y = X2, x = reorder(X1, -X2))) +
    coord_flip() +
    labs(x = "Session", y = "Number of Registered Participants")
