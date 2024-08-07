# Chương Trình Tính Toán Và Phân Tích Điểm Thi

## Tổng Quan

Dự án này sẽ giúp giáo viên chấm bài nhanh hơn cho các lớp học đông học sinh. Nó sẽ đọc các bài làm tử học sinh, đảm bảo tính hợp lệ của dữ liệu, chấm điểm và đưa ra báo cáo chi tiết. Điều này sẽ giúp giáo viên tiết kiệm thời gian và hiểu được học sinh đang học tốt như thế nào.

## Tính Năng

1. **Xử Lý Tệp Tin Với Quản Lý Ngoại Lệ**: Mở và đọc tệp văn bản một cách an toàn, xử lý trường hợp tệp không tồn tại.
2. **Kiểm Tra Dữ Liệu**: Phân tích từng dòng dữ liệu bài làm để xác định tính hợp lệ và báo cáo các lỗi nếu có.
3. **Chấm Điểm**: Chấm điểm từng bài thi dựa trên đáp án chuẩn, tính đến các câu trả lời đúng, sai và bỏ trống.
4. **Báo Cáo**: Tạo các báo cáo chi tiết, bao gồm:
    - Tổng số dòng dữ liệu hợp lệ và không hợp lệ
    - Điểm của từng học sinh
    - Thống kê tổng quan (điểm cao nhất, thấp nhất, trung bình, và trung vị)
    - Các câu hỏi bị bỏ qua nhiều nhất hoặc trả lời sai nhiều nhất
5. **Xuất File**: Lưu kết quả chấm điểm vào các tệp CSV và văn bản có tên phù hợp để phân tích và lưu trữ.

## Yêu Cầu

- Python 3.x 
- Pandas
- NumPy

## Cài Đặt

Đảm bảo bạn đã cài đặt Python 3 và các thư viện cần thiết.

## Sử Dụng

1. Đặt Các Tệp Dữ Liệu
Lưu các tệp văn bản chứa bài làm của học sinh vào một thư mục chỉ định trên máy tính của bạn. Đảm bảo rằng mỗi tệp có tên phù hợp với lớp học, trong projet này có 8 file điểm của 8 lớp từ class1.txt đến class8.txt.

2. Chạy Chương Trình
Thực thi script và nhập tên lớp khi được yêu cầu. Đảm bảo rằng tệp lastname_firstname_grade_the_exams.py nằm cùng thư mục với các tệp dữ liệu.

3. Nhập Tên Lớp
Khi được yêu cầu, nhập tên tệp lớp (ví dụ: class1 cho tệp class1.txt).

Ví dụ:

Enter a class name to grade (i.e. class1 for class1.txt): class1
Chương trình sẽ xử lý tệp class1.txt, kiểm tra dữ liệu, chấm điểm từng bài thi, và tạo báo cáo.

## Kết Quả

Chương trình sẽ tạo ra các file kết quả sau:

class1_grades.txt: File văn bản chứa điểm của từng học sinh.

Báo cáo chi tiết về các câu hỏi bị bỏ qua nhiều nhất hoặc trả lời sai nhiều nhất.

## Đóng Góp

Nếu bạn muốn đóng góp cho dự án, vui lòng tạo pull request hoặc báo lỗi tại repository trên GitHub.
