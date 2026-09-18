# import and global variables

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

from kivy.core.window import Window

import os


# window size

Window.size = (450, 550)


# Image Gallery Provider

class ImageGalleryProvider:

    # image folder

    image_folder = "images"


    # function for reading images from folder

    def get_images(self):

        # check if folder exists

        if not os.path.exists(
            self.image_folder
        ):

            return []


        # supported image formats

        image_extensions = (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp"
        )


        # get image files

        images = []

        for filename in os.listdir(
            self.image_folder
        ):

            if filename.lower().endswith(
                image_extensions
            ):

                image_path = os.path.join(
                    self.image_folder,
                    filename
                )

                images.append(
                    image_path
                )


        # sort images

        images.sort()


        return images


# main application

class GalleryGUIApp(App):


    # build the application UI

    def build(self):

        # create main layout

        main_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        # application title

        title_label = Label(
            text="Photo Gallery",
            font_size=32,
            size_hint_y=None,
            height=60
        )


        # image widget

        self.image_widget = Image(
            source="",
            allow_stretch=True,
            keep_ratio=True
        )


        # image information label

        self.info_label = Label(
            text="No image selected.",
            font_size=18,
            size_hint_y=None,
            height=45
        )


        # previous button

        previous_button = Button(
            text="Previous Image",
            size_hint_y=None,
            height=50
        )


        previous_button.bind(
            on_press=self.previous_image
        )


        # next button

        next_button = Button(
            text="Next Image",
            size_hint_y=None,
            height=50
        )


        next_button.bind(
            on_press=self.next_image
        )


        # status label

        self.status_label = Label(
            text="Ready",
            font_size=16,
            size_hint_y=None,
            height=40
        )


        # add widgets to main layout

        main_layout.add_widget(
            title_label
        )

        main_layout.add_widget(
            self.image_widget
        )

        main_layout.add_widget(
            self.info_label
        )

        main_layout.add_widget(
            previous_button
        )

        main_layout.add_widget(
            next_button
        )

        main_layout.add_widget(
            self.status_label
        )


        # create image provider

        self.provider = ImageGalleryProvider()


        # get images from folder

        self.images = (
            self.provider.get_images()
        )


        # default image index

        self.current_index = 0


        # show first image

        self.show_image()


        return main_layout


    # function for showing current image

    def show_image(self):

        # check if there are images

        if not self.images:

            self.image_widget.source = ""

            self.info_label.text = (
                "No images found."
            )

            self.status_label.text = (
                "Please add images to the images folder."
            )

            return


        # get current image

        image_path = (
            self.images[
                self.current_index
            ]
        )


        # show image

        self.image_widget.source = (
            image_path
        )


        # get image filename

        image_name = os.path.basename(
            image_path
        )


        # create image information

        self.info_label.text = (
            f"Image {self.current_index + 1} "
            f"of {len(self.images)}\n"
            f"{image_name}"
        )


        # update status

        self.status_label.text = (
            "Image displayed."
        )


    # function for showing next image

    def next_image(self, instance):

        # check if there are images

        if not self.images:

            self.status_label.text = (
                "No images available."
            )

            return


        # move to next image

        self.current_index += 1


        # return to first image

        if self.current_index >= len(
            self.images
        ):

            self.current_index = 0


        # display image

        self.show_image()


    # function for showing previous image

    def previous_image(self, instance):

        # check if there are images

        if not self.images:

            self.status_label.text = (
                "No images available."
            )

            return


        # move to previous image

        self.current_index -= 1


        # go to last image

        if self.current_index < 0:

            self.current_index = (
                len(self.images) - 1
            )


        # display image

        self.show_image()


# run application

if __name__ == "__main__":

    GalleryGUIApp().run()