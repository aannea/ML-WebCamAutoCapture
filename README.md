# Machine Learning WebCam Auto Capture

## Import Library:
import cv2
import mediapipe as mp
import os
import time
cv2: Library OpenCV untuk pengolahan citra dan video.
mediapipe: Library MediaPipe yang menyediakan solusi deteksi pose tangan.

## Fungsi detect_pose:
def detect_pose(landmarks):
Fungsi ini menerima landmark tangan dari MediaPipe dan mengembalikan pose tangan yang terdeteksi (OK, Thumbs Up, Peace, Rock, atau None jika tidak ada pose yang terdeteksi).

## Fungsi capture_images:
def capture_images(output_folder, num_images=1):
Fungsi ini menginisialisasi webcam, menggunakan MediaPipe untuk deteksi pose, dan menyimpan gambar saat pose tertentu terdeteksi. Gambar-gambar disimpan dalam folder yang ditentukan.

## Panggilan Fungsi di __main__:
if __name__ == "__main__":
    output_folder = "captured_images"
    capture_images(output_folder)
Bagian ini menjalankan program ketika skrip dijalankan secara langsung. Folder output diatur menjadi "captured_images", dan fungsi capture_images dipanggil.

## Loop Utama:
while True:
Program berada dalam loop utama yang terus berjalan selama webcam aktif. Setiap iterasi loop, program membaca frame dari webcam, mendeteksi pose tangan, dan mengambil gambar jika pose tertentu terdeteksi.

## Menyimpan Gambar:
cv2.imwrite(image_path, frame)
Saat pose yang diinginkan terdeteksi, program menyimpan frame saat itu sebagai gambar JPEG di folder output.

## Menampilkan Hasil:
cv2.imshow("Webcam", frame)
Frame aktual dari webcam ditampilkan di jendela.

## Penghentian Program:
if key == ord('q'):
    break
Program dapat dihentikan dengan menekan tombol 'q'.

## Penjelasan Tambahan:
Setelah gambar diambil, teks "Diambil!" ditambahkan pada frame untuk memberi tahu pengguna.
Waktu terakhir gambar diambil diperbarui untuk menghindari pengambilan gambar yang berlebihan.
Program dapat disesuaikan untuk mendeteksi pose lain atau untuk mengambil gambar dengan interval waktu yang berbeda.
