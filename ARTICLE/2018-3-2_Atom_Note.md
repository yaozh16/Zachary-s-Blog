# Atom package
## flow
* Atom starts up
* Atom starts loading packages
* Atom reads your package.json
* Atom loads keymaps, menus, styles and the main module
* Atom finishes loading packages
* At some point, the user executes your package command your-name-word-count:toggle
* Atom executes the activate method in your main module which sets up the UI by creating the hidden modal view
* Atom executes the package command your-name-word-count:toggle which reveals the hidden modal view
* At some point, the user executes the your-name-word-count:toggle command again
* Atom executes the command which hides the modal view
* Eventually, Atom is shut down which can trigger any serializations that your package has defined
