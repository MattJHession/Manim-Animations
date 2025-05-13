# Derivative Visualization with Manim

## Overview

This project is a mathematical animation created using the Manim Python library. It visually demonstrates the concept of a derivative as the slope of the tangent line, starting with secant lines and dynamically transitioning to the tangent using `ValueTracker`.

## Tools Used

- Python (Manim library)
- LaTeX (for math labeling)
- FFmpeg (for video rendering)

## Features

- Dynamic secant/tangent transition
- Custom axes and labeled functions
- 3D camera movement for enhanced visualization
- Aligned with concepts from Real Analysis and Calculus

## Output

The animation renders as an `.mp4` video. See the `media/` folder or view a sample [here](#) *(link to video or gif if available)*.

## How to Run

```bash
manim -pqh full_derivative_animation.py FullDerivativeAnimation
