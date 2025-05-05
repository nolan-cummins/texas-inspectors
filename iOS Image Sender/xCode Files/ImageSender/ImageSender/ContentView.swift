import SwiftUI

struct ContentView: View {
    @State private var selectedImage: UIImage?
    @State private var isPickerPresented = false
    @ObservedObject private var webSocketManager = WebSocketManager()

    var body: some View {
        VStack {
            Text("Welcome to Texas Investigators Camera App!")
            
            Spacer().frame(height: 100)
            
            if let image = selectedImage {
                Image(uiImage: image)
                    .resizable()
                    .scaledToFit()
                    .frame(height: 300)
                    .cornerRadius(12)
                    .padding()
            }

            Button("Take Photo") {
                webSocketManager.sendMessage()
                isPickerPresented = true
            }
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .clipShape(RoundedRectangle(cornerRadius: 10))

            if selectedImage != nil {
                Button("Send to Server") {
                    if let image = selectedImage, let imageData = image.jpegData(compressionQuality: 0.8) {
                        webSocketManager.sendImage(imageData)
                    }
                }
                .padding()
                .background(Color.green)
                .foregroundColor(.white)
                .clipShape(RoundedRectangle(cornerRadius: 10))
            }
        }
        .sheet(isPresented: $isPickerPresented) {
            ImagePicker(image: $selectedImage)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
