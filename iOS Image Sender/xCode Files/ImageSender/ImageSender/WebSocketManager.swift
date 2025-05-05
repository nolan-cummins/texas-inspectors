import Foundation

class WebSocketManager: ObservableObject {
    private var webSocketTask: URLSessionWebSocketTask?

    init() {
        connect()
    }

    func connect() {
        let url = URL(string: "ws://172.30.2.4:8765")! // check local IP
        webSocketTask = URLSession.shared.webSocketTask(with: url)
        webSocketTask?.resume()
    }

    func sendImage(_ imageData: Data) {
        let message = URLSessionWebSocketTask.Message.data(imageData)
        webSocketTask?.send(message) { error in
            if let error = error {
                print("Error sending image: \(error)")
            } else {
                print("Image sent successfully")
            }
        }
    }
    
    func sendMessage() {
            let message = URLSessionWebSocketTask.Message.string("Hello from iOS!")
            webSocketTask?.send(message) { error in
                if let error = error {
                    print("Error sending message: \(error)")
                } else {
                    print("Message sent successfully")
                }
            }
        }


    func disconnect() {
        webSocketTask?.cancel(with: .goingAway, reason: nil)
    }
}
