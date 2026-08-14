import json
import os

def load_notes():
    # اگه فایل وجود نداشته باشه (اولین اجرای برنامه)، لیست خالی برگردون
    if not os.path.exists("notes.json"):
        return []
    with open("notes.json", "r") as f:
        return json.load(f)


def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f)


def add_note(notes):
    text = input("متن یادداشت رو وارد کن: ")
    # id رو بر اساس تعداد یادداشت‌های فعلی می‌سازیم
    new_id = len(notes) + 1
    note = {"id": new_id, "text": text}
    notes.append(note)
    return notes


def show_notes(notes):
    if not notes:
        print("هیچ یادداشتی ثبت نشده.")
        return
    for note in notes:
        print(f"[{note['id']}] {note['text']}")


def delete_note(notes):
    note_id = int(input("id یادداشتی که می‌خوای حذف کنی رو وارد کن: "))
    # فقط یادداشت‌هایی رو نگه می‌داریم که id شون با ورودی کاربر یکی نیست
    notes = [n for n in notes if n["id"] != note_id]
    return notes


def main():
    notes = load_notes()

    while True:
        print("\n=== Notes CLI ===")
        print("1. افزودن یادداشت")
        print("2. نمایش یادداشت‌ها")
        print("3. حذف یادداشت")
        print("4. خروج")
        choice = input("انتخابت: ")

        if choice == "1":
            notes = add_note(notes)
            save_notes(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            notes = delete_note(notes)
            save_notes(notes)
        elif choice == "4":import json
import os

def load_notes():
    # اگه فایل وجود نداشته باشه (اولین اجرای برنامه)، لیست خالی برگردون
    if not os.path.exists("notes.json"):
        return []
    with open("notes.json", "r") as f:
        return json.load(f)


def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f)


def add_note(notes):
    text = input("متن یادداشت رو وارد کن: ")
    # id رو بر اساس تعداد یادداشت‌های فعلی می‌سازیم
    new_id = len(notes) + 1
    note = {"id": new_id, "text": text}
    notes.append(note)
    return notes


def show_notes(notes):
    if not notes:
        print("هیچ یادداشتی ثبت نشده.")
        return
    for note in notes:
        print(f"[{note['id']}] {note['text']}")


def delete_note(notes):
    note_id = int(input("id یادداشتی که می‌خوای حذف کنی رو وارد کن: "))
    # فقط یادداشت‌هایی رو نگه می‌داریم که id شون با ورودی کاربر یکی نیست
    notes = [n for n in notes if n["id"] != note_id]
    return notes


def main():
    notes = load_notes()

    while True:
        print("\n=== Notes CLI ===")
        print("1. افزودن یادداشت")
        print("2. نمایش یادداشت‌ها")
        print("3. حذف یادداشت")
        print("4. خروج")
        choice = input("انتخابت: ")

        if choice == "1":
            notes = add_note(notes)
            save_notes(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            notes = delete_note(notes)
            save_notes(notes)
        elif choice == "4":
            break
        else:
            print("ورودی نامعتبره، دوباره امتحان کن.")


if __name__ == "__main__":
    main()
            break
        else:
            print("ورودی نامعتبره، دوباره امتحان کن.")


if __name__ == "__main__":
    main()