# Gerekli kütüphaneler içe aktarılıyor
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

# Veri dosyası okunuyor
data = pd.read_csv('diabetes.csv')

# İlk 3 satırı görüntüleyerek veri setine genel bir bakış sağlanıyor
data.head(3)

# Özellikler (X) ve etiket (Y) olarak veri ayrılıyor
X = data.drop(columns='Outcome', axis=1)  # 'Outcome' dışındaki sütunlar giriş verisi olarak alınıyor
Y = data['Outcome']  # 'Outcome' sütunu hedef değişken olarak alınıyor

# Veriler standardize ediliyor (ölçekleme)
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)  # Bu adımda veriler normalize edilmiş oluyor

# Veri eğitim ve test olarak ayrılıyor (stratify=Y, sınıf dağılımının korunmasını sağlar)
X=standardized_data
Y=data['Outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, 
                                                    stratify=Y, random_state=42)

# Lineer çekirdekli Support Vector Machine (SVM) sınıflandırıcısı oluşturuluyor
classifier = svm.SVC(kernel='linear')

# SVM modeli eğitim verileri ile eğitiliyor
classifier.fit(X_train, Y_train)

# Eğitim verileri üzerindeki tahminler ve doğruluk skoru hesaplanıyor
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data : ', training_data_accuracy)

# Test verileri üzerindeki tahminler ve doğruluk skoru hesaplanıyor
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data : ', test_data_accuracy)

# Ek performans metrikleri (opsiyonel ama önerilir)
print("\nConfusion Matrix:\n", confusion_matrix(Y_test, X_test_prediction))
print("\nClassification Report:\n", classification_report(Y_test, X_test_prediction))
import joblib

# Eğitilen modeli .pkl dosyasına kaydet
joblib.dump(classifier, 'svm_diabetes_model.pkl')
print("Model başarıyla 'svm_diabetes_model.pkl' olarak kaydedildi.")

