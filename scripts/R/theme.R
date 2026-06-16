#' Shared theme constants for figures and plots.
#'
#' Okabe-Ito colorblind-friendly palette.
#' Mirrors the LaTeX definitions in latex_preambles/header_slides.tex and header_doc.tex.

OKABE_ITO <- c(
  black      = "#000000",
  orange     = "#E69F00",
  sky_blue   = "#56B4E9",
  green      = "#009E73",
  yellow     = "#F0E442",
  blue       = "#0072B2",
  vermillion = "#D55E00",
  purple     = "#CC79A7"
)

#' Base colors used in theme_custom()
black      <- "#000000"
white      <- "#FFFFFF"
gray_light1 <- "#D9D9D9"

#' Minimal ggplot2 theme for publication-quality figures.
#' Requires ggplot2 to be loaded.
theme_custom <- function() {

  theme_minimal() %+replace%
    theme(
      text             = element_text(
        face           = "plain",
        lineheight     = 1.2
      ),
      panel.background = element_rect(fill = white, color = white, linewidth = 0.5, linetype = "solid"),
      panel.grid.major = element_line(color = gray_light1, linewidth = 0.3, linetype = 2),
      panel.grid.minor = element_blank(),
      panel.border     = element_rect(fill = NA, color = black, linewidth = 0.5, linetype = "solid"),
      plot.background  = element_rect(fill = white, color = white),
      legend.title     = element_blank(),
      legend.text      = element_text(size = 9.5, color = black),
      legend.key.width = unit(1, "cm"),
      legend.key       = element_rect(fill = "transparent", color = "transparent"),
      axis.title       = element_text(size = 10, color = black),
      axis.text        = element_text(size = 9, color = black),
      plot.title       = element_text(size = 10, face = "bold", color = black),

      complete         = TRUE
    )

}
